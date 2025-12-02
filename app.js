async function checkDomain(domain) {
    const API_KEY = "OIgCwJbtkk0tSMngejuZkw==pXAxvfDzvOnxrBKe";
    const url = `https://api.api-ninjas.com/v1/whois?domain=${domain}`;

    try {
        const response = await fetch(url, {
            headers: { "X-Api-Key": API_KEY }
        });

        const data = await response.json();

        // Eğer API hata dönerse → domain büyük ihtimalle boş
        if (!data || data.error || data.is_available === true) {
            return "AVAILABLE";
        }

        // WHOIS datası varsa → domain %100 alınmış
        if (
            data.domain_name ||
            data.creation_date ||
            data.created ||
            data.registrar ||
            (data.name_servers && data.name_servers.length > 0)
        ) {
            return "TAKEN";
        }

        // Veri yok → boş domain
        return "AVAILABLE";

    } catch (err) {
        console.log("Hata:", err);
        return "UNKNOWN";
    }
}
