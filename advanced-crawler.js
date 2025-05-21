/** @param {NS} ns **/
export async function main(ns) {
  const graph = {};
  const visited = new Set();
  const paths = {};
  const serverInfo = {};

  // DFS to build the graph and store path info
  function dfs(server, path = []) {
    visited.add(server);
    const neighbors = ns.scan(server);
    graph[server] = neighbors;
    paths[server] = [...path, server];

    // Collect metadata
    serverInfo[server] = {
      root: ns.hasRootAccess(server),
      hackLevel: ns.getServerRequiredHackingLevel(server),
      maxMoney: ns.getServerMaxMoney(server),
      ram: ns.getServerMaxRam(server),
      serverGrowth: ns.getServerGrowth(server),
      securityLevel: ns.getServerSecurityLevel(server),
      minSecurityLevel: ns.getServerMinSecurityLevel(server),
      backdoor: ns.getServer(server).backdoorInstalled,
      path: [...path, server]
    };



    for (const neighbor of neighbors) {
      if (!visited.has(neighbor)) {
        dfs(neighbor, paths[server]);
      }
    }
  }

  dfs("home");

  // Sort servers by maxMoney for viable targets
  const hackableTargets = Object.entries(serverInfo)
    .filter(([name, info]) =>
      info.root &&
      info.maxMoney > 0 &&
      info.hackLevel <= ns.getHackingLevel()
    )
    .sort((a, b) => b[1].maxMoney - a[1].maxMoney)
    .map(([name, info]) => ({
      name,
      money: info.maxMoney,
      hackLevel: info.hackLevel,
      path: info.path,
    }));

  // Output and save to files
  await ns.write("crawling/network-graph.json", JSON.stringify(graph, null, 2), "w");
  await ns.write("crawling/server-info.json", JSON.stringify(serverInfo, null, 2), "w");
  await ns.write("crawling/hack-targets.json", JSON.stringify(hackableTargets, null, 2), "w");

  ns.tprint(`✅ Network scan complete!`);
  ns.tprint(`🧠 Servers scanned: ${Object.keys(graph).length}`);
  ns.tprint(`🎯 Hackable targets found: ${hackableTargets.length}`);
  ns.tprint(`📁 Output written to: network-graph.json, server-info.json, hack-targets.json`);
}
