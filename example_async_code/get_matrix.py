from matrix_crawler import get_matrix
import asyncio


SOURCE_URL = (
              'https://raw.githubusercontent.com/avito-tech/'
              'python-trainee-assignment/main/matrix.txt'
)
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

print(asyncio.run(get_matrix(SOURCE_URL)))
