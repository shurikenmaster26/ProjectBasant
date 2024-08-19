// JavaScript to toggle mute/unmute
function toggleMute() {
    var video = document.getElementById('bgVideo');
    var buttonText = document.getElementById('buttonText');
    
    if (video.muted) {
        video.muted = false;
        buttonText.textContent = 'Mute';
    } else {
        video.muted = true;
        buttonText.textContent = 'Unmute';
    }
}
