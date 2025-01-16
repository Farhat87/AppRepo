function adjustPageScale() {
    const screenWidth = window.innerWidth;
    const bodyElement = document.body;

    if (screenWidth >= 992 && screenWidth <= 1600) {
        bodyElement.style.transform = "scale(0.9)";
        bodyElement.style.transformOrigin = "top left";
    } else if (screenWidth >= 700 && screenWidth <= 767) {
        bodyElement.style.transform = "scale(0.8)";
        bodyElement.style.transformOrigin = "top left";
    } else if (screenWidth >= 600 && screenWidth < 700) {
        bodyElement.style.transform = "scale(0.75)";
        bodyElement.style.transformOrigin = "top left";
    } else if (screenWidth <= 600) {
        bodyElement.style.transform = "scale(0.5)";
        bodyElement.style.transformOrigin = "top left";
    } else {
        bodyElement.style.transform = "scale(1)";  // Default scale for larger screens
    }
}

// Call the function on page load
window.onload = adjustPageScale;

// Add an event listener to handle window resizing
window.onresize = adjustPageScale;
