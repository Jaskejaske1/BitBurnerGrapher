# BitBurnerGrapher
 A server grapher for BitBurner

1. Run `advanced-crawler.js` on BitBurner.
2. Copy the three generated `.json` files: `network-graph.json`, `server-info.json` and `hack-targets.json` from BitBurner to the root directory of this repository.
3. Serve the root directory of this repository with an HTTP server to localhost and browse to the graph.
4. For example you can use the built in python HTTP server:
    - run: `python -m http.server`
    - go to http://localhost:8000/cytoscape-graph-7.html in your web browser of choice.

Side note: I leveraged some example `.json` files but I encourage you to replace them with your own.