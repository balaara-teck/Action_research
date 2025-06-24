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
// Floating Share Button functionality
   function getShareContent() {
    const title = "Check out this awesome site!"; // You can customize this
    const url = "http://0.0.0.0:8000/"; // Static URL for sharing
    return {
        title: encodeURIComponent(title),
        url: encodeURIComponent(url)
    };
}

// Function to share on Facebook
function shareOnFacebook() {
    const { url, title } = getShareContent();
    const shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}&quote=${title}`;
    window.open(shareUrl, '_blank');
}

// Function to share on Twitter
function shareOnTwitter() {
    const { url, title } = getShareContent();
    const shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
    window.open(shareUrl, '_blank');
}

// Function to share on WhatsApp
function shareOnWhatsApp() {
    const { url, title } = getShareContent();
    const shareUrl = `https://api.whatsapp.com/send?text=${title}%0A%0A${url}`;
    window.open(shareUrl, '_blank');
}

// Function to copy link to clipboard
function copyLink() {
    const { url, title } = getShareContent();
    const textToCopy = `${decodeURIComponent(title)}\n${decodeURIComponent(url)}`;
    
    navigator.clipboard.writeText(textToCopy).then(() => {
        const copyBtn = document.getElementById('copyLinkBtnFloat');
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="bi bi-check"></i> Copied!';
        setTimeout(() => {
            copyBtn.innerHTML = originalText;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
        alert('Failed to copy link');
    });
}

    function toggleShareOptions() {
        const shareOptions = document.getElementById('shareOptionsFloat');
        shareOptions.classList.toggle('show');
    }

    // Close share options when clicking outside
    document.addEventListener('click', function(event) {
        const shareOptions = document.getElementById('shareOptionsFloat');
        const floatingShareBtn = document.querySelector('.floating-share-btn');
        
        if (!shareOptions.contains(event.target) && !floatingShareBtn.contains(event.target)) {
            shareOptions.classList.remove('show');
        }
    });

    


 