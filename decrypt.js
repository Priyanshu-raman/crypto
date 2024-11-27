async function decryptMessage() {
  const encryptedMessageInput = document.querySelector(
    ".encrypted-message-input"
  ).value;
  const keyInput = document.querySelector(".key-input").value;
  const outputTextarea = document.querySelector(".output");

  if (!encryptedMessageInput || !keyInput) {
    alert("Please enter both the encrypted message and the key.");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/decrypt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        encrypted_message: encryptedMessageInput,
        key: keyInput,
      }),
    });

    if (!response.ok) {
      console.log("not working");
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    if (data.error) {
      alert(data.error);
    } else {
      outputTextarea.value = data.decrypted_message;
    }
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
  }
}
