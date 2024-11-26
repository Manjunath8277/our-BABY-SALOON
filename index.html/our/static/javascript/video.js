document.addEventListener("DOMContentLoaded", function () {
    const leftPanelVideo = document.querySelector(".left-panel .image");
    const rightPanelVideo = document.querySelector(".right-panel .image");
    const formsContainer = document.querySelector(".forms-container");
  
    function moveVideos() {
      const screenWidth = window.innerWidth;
  
      if (screenWidth <= 767) {
        if (!formsContainer.contains(leftPanelVideo)) {
          formsContainer.appendChild(leftPanelVideo);
        }
        if (!formsContainer.contains(rightPanelVideo)) {
          formsContainer.appendChild(rightPanelVideo);
        }
      } else {
        // Return videos to their original locations if the screen size increases
        const leftPanel = document.querySelector(".left-panel");
        const rightPanel = document.querySelector(".right-panel");
        if (!leftPanel.contains(leftPanelVideo)) {
          leftPanel.appendChild(leftPanelVideo);
        }
        if (!rightPanel.contains(rightPanelVideo)) {
          rightPanel.appendChild(rightPanelVideo);
        }
      }
    }
  
    // Call the function on page load and when resizing the window
    moveVideos();
    window.addEventListener("resize", moveVideos);
  });