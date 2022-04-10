# CompareIt Node.js API

Python crawler with Node API to crawl for products, returns product details in JSON format.

## Crawler set up:
1. Create a folder in your local computer.
2. Clone repository with <code>git clone https://github.com/tamysiby/compareit-node.git </code>
3. <code>cd compareit-node</code>
4. Run <code>npm install</code> to install dependencies.
5. Run <code>npm start</code> to start server
6. Server will be running in http://localhost:5000

## How to use crawler in client side:
Set up front end to receive data from get from '/crawl/${searchInput}'

Example: 
<code>const response = await axios.get(\`http://localhost:5000/crawl/${searchInput}`);</code>

Returned <code>response</code> will be json.

## Future development:
1. Database to save previously searched data to improve performance
2. Database for the user auth information

## Additional resources:
1. Frontend code with complete documentation https://github.com/debdeb18/compareit-frontend-react
2. Application demo: https://youtu.be/R0_mhcd8MY4
