from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='CN8EEI4TXZFFMTXWI395LPS3E6MJICGPBBVYVUTPEYBZI58BI6F8WGE6HDGG60QNJRF3DG4PGVY9DYBY')

response = client.get("https://app.scrapingbee.com/api/v1/usage", block_resources=False)

answer = response.content

print(answer)