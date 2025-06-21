const phrases = [
    "Hello!",
    "Only Action Research",
    "Just Action Research",
    "My Action Research"
];

let currentIndex = 0;
const dynamicTextElement = document.getElementById('dynamic-text');

// Function to update the text
function changeText() {
    dynamicTextElement.textContent = phrases[currentIndex];
    currentIndex = (currentIndex + 1) % phrases.length; // Loop through the phrases
}

setInterval(changeText, 5000);
changeText();



// for whatsapp communications
function showChatPopup() {
    const confirmChat = confirm("Do you want to chat Project Analyst for your project?\nUnable to open Whatsapp automatically, chat manually on 0266342915");
    if (!confirmChat) return;

    const phone = "233266342915";
    const message = encodeURIComponent("Hello Sir, I need help with my project, please.");
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    if (isMobile) {
      window.location.href = `https://wa.me/${phone}?text=${message}`;
    } else {
      const desktopUrl = `whatsapp://send?phone=${phone}&text=${message}`;
      const webUrl = `https://web.whatsapp.com/send?phone=${phone}&text=${message}`;
      const iframe = document.createElement('iframe');
      iframe.style.display = 'none';
      iframe.src = desktopUrl;
      
      document.body.appendChild(iframe);
      setTimeout(() => {
        window.open(webUrl, '_blank');
        document.body.removeChild(iframe);
      }, 2000); 
    }
  }

 