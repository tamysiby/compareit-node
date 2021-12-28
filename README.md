# compareit-node

Python crawler with Node API to crawl for products, returns product details in JSON format.

How to use crawler:
Set up front end to receive data from get from '/crawl/${searchInput}'

Example:<br>
`const response = await axios.get(`http://localhost:5000/crawl/${searchInput}`);`

`response` will be json.
