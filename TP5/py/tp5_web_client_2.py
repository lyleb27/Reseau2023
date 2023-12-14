import http.client

host = "127.0.0.1"
port = 8000

conn = http.client.HTTPConnection(host, port)

conn.request("GET", "/")

response = conn.getresponse()

print(f"Response Status: {response.status}")
print("Response Content:")
print(response.read().decode())

conn.close()
