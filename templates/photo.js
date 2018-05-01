(function(){
  var video = document.getElementById('video'),
      vendorlUrl = window.URL || window.webkitURL;

      navigator.getMedia = navigator.getUserMedia ||
                            navigator.webkitGetUserMedia ||
                            navigator.mozGetUserMedia ||
                            navigator.msGetUserMedia;

      navigator.getMedia({
        video: true,
        audio: false
      }, function(stream){
            video.src = vendorlUrl.createObjectUrl;
            video.play();
      }, function(error){
        // An error occured
        //error.code

      });
})();
