function predictPrice() {

    const brand = document.getElementById("brand").value;
    const ram = document.getElementById("ram").value;
    const storage = document.getElementById("storage").value;
    const resultBox = document.getElementById("result");

    if (brand === "" || ram === "" || storage === "") {
        resultBox.innerText = "⚠️ Please fill all fields";
        return;
    }

    const data = {
        Brand: brand,
        RAM_Size: parseFloat(ram),
        Storage_Capacity: parseFloat(storage)
    };

    resultBox.innerText = "⏳ Predicting...";

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        resultBox.innerText = "💰 Predicted Price: ₹ " + result.predicted_price;
    })
    .catch(() => {
        resultBox.innerText = "❌ Error predicting price";
    });
}
