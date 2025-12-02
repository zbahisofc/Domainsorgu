async function checkDomain(domain) {
    const API_KEY = "OIgCwJbtkk0tSMngejuZkw==pXAxvfDzvOnxrBKe"; // api-ninjas key buraya
    const url = `https://api.api-ninjas.com/v1/whois?domain=${domain}`;

    try {
        const response = await fetch(url, {
            headers: { 'X-Api-Key': API_KEY }
        });

        const data = await response.json();

        if (data.error) {
            return "UNKNOWN";
        }

        return data.created ? "TAKEN" : "AVAILABLE";

    } catch (e) {
        return "ERROR";
    }
}

async function startScan() {
    const prefix = document.getElementById("prefix").value;
    const start = parseInt(document.getElementById("start").value);
    const end = parseInt(document.getElementById("end").value);
    const tld = document.getElementById("tld").value;

    const resultBox = document.getElementById("result");
    resultBox.innerHTML = "Scanning...<br><br>";

    for (let i = start; i <= end; i++) {
        const domain = `${prefix}${i}${tld}`;
        const status = await checkDomain(domain);

        let statusClass = status === "AVAILABLE" ? "available" : "taken";

        resultBox.innerHTML += `<span class="${statusClass}">${domain} → ${status}</span><br>`;
    }
}
