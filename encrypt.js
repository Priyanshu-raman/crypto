async function encryptMessage() {
  const messageInput = document.querySelector(".message-input").value;
  const outputTextarea = document.querySelector(".output");
  const keyTextarea = document.querySelector(".key-output");

  if (!messageInput) {
    alert("Please enter a message to encrypt.");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/encrypt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: messageInput }),
    });

    if (!response.ok) {
      console.log("not workign");
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    if (data.error) {
      //   console.log("saddadsd");
      alert(data.error);
    } else {
      outputTextarea.value = data.encrypted_message;
      keyTextarea.value = data.key;
    }
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
  }
}

function show() {
  const keyfield = document.querySelector(".key-output");
  if (keyfield.type == "password") {
    keyfield.type = "text";
  } else {
    keyfield.type = "password";
  }
}

function copyText() {
  const outputTextarea = document.querySelector(".output").value;
  navigator.clipboard.writeText(outputTextarea);
}

function copyKey() {
  const key = document.querySelector(".key-output").value;
  navigator.clipboard.writeText(key);
}
