import os


from dotenv import load_dotenv
print(load_dotenv())
print(os.environ.get('USE_S3'))

print(os.getcwd())