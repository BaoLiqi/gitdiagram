import os

# Set the 'all_proxy' environment variable
os.environ['all_proxy'] = "http://127.0.0.1:7890/"

# (Optional) Verify that it's set correctly
print("all_proxy is set to:", os.environ.get('all_proxy'))
