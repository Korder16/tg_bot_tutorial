import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    admins = os.getenv('ADMINS')
    print(f'{admins=}')

if __name__ == '__main__':
    main()