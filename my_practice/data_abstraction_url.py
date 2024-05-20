# Implement an abstraction for working with URLs.
# It should extract and change parts of the address.
#
# Interface:
#
# make(url) - Constructor. Creates a URL.
# get_scheme(data) - Selector (getter). Extracts the scheme.
# set_scheme(data, scheme) - Setter. Changes the scheme.
# get_host(data) - Getter. Extracts the host.
# set_host(data, host) - Setter. Changes the host.
# get_path(data) - Getter. Extracts the path.
# set_path(data, path) - Setter. Changes the path.
# get_query_param(data, param_name, default=None) - Getter.
# Extracts the value for a query parameter.
# The third parameter is the default value,
# which is returned when the query does not have such a parameter.
# set_query_param(data, key, value) - Setter.
# Sets the value for a query parameter.
# If None is passed as a value, the parameter is discarded.
# to_string(data) - Getter. Converts the URL to a string.
# All setters must return a new modified URL, leaving the old one unchanged.


# Реализуйте абстракцию для работы с URL.
# Она должна извлекать и менять части адреса.
#
# Интерфейс:
#
# make(url) - Конструктор. Создает URL.
# get_scheme(data) - Селектор (геттер). Извлекает схему.
# set_scheme(data, scheme) - Сеттер. Меняет схему.
# get_host(data) - Геттер. Извлекает host.
# set_host(data, host) - Сеттер. Меняет host.
# get_path(data) - Геттер. Извлекает путь.
# set_path(data, path) - Сеттер. Меняет путь.
# get_query_param(data, param_name, default=None) - Геттер.
# Извлекает значение для параметра запроса.
# Третьим параметром функция принимает значение по умолчанию,
# которое возвращается тогда, когда в запросе не было такого параметра
# set_query_param(data, key, value) - Сеттер.
# Устанавливает значение для параметра запроса.
# Если передано значение None, то параметр отбрасывается.
# to_string(data) - Геттер. Преобразует URL в строковой вид.
# Все сеттеры должны возвращать новый изменённый URL,
# а старый оставлять неизменным.
#
# Example:
#
# import url
# u = url.make('https://hexlet.io/community?q=low')
#
# u = url.set_scheme(u, 'http')
# url.to_string(u)  # 'http://hexlet.io/community?q=low'
#
# u = url.set_path(u, '/404')
# url.to_string(u)  # 'http://hexlet.io/404?q=low'
#
# url.get_query_param(u, 'q')  # 'low'
#
# u = url.set_query_param(u, 'page', 5)
# url.to_string(u)  # 'http://hexlet.io/404?q=low&page=5'
#
# u = url.set_query_param(u, 'q', 'high')
# url.to_string(u)  # 'http://hexlet.io/404?q=high&page=5'
#
# u = url.set_query_param(u, 'q', None)
# url.to_string(u)  # 'http://hexlet.io/404?page=5'


from urllib.parse import parse_qs, urlparse, urlencode, urlunparse


def make(url):
    return urlparse(url)


def get_scheme(data):
    return data.scheme


def set_scheme(data, scheme):
    return data._replace(scheme=scheme)


def get_host(data):
    return data.netloc


def set_host(data, host):
    return data._replace(netloc=host)


def get_path(data):
    return data.path


def set_path(data, path):
    return data._replace(path=path)


def get_query_param(data, param_name, default=None):
    result = parse_qs(data.query).get(param_name, [default])[0]
    return result


def set_query_param(data, key, value):
    params = parse_qs(data.query, keep_blank_values=True)
    if value is not None:
        params[key] = [value]
    else:
        params.pop(key, None)
    new_query = urlencode(params, doseq=True)
    return data._replace(query=new_query)


def to_string(data):
    return urlunparse(data)
