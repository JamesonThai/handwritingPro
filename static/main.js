// function grabVideo(){

// Grab elements, create settings, etc.
var video = document.getElementById('video');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    // navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
    //     // video.src = window.URL.createObjectURL(stream);
    //     // video.play();

    // });
    navigator.getMedia = (navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia);
    navigator.getMedia(
        // constraints
        {video:true, audio:false},
        // success callback
        function (mediaStream) {
            var video = document.getElementsByTagName('video')[0];
            video.src = window.URL.createObjectURL(mediaStream);
            video.play();
        },    
}

    // var canvas = document.getElementById('canvas');
    // var context = canvas.getContext('2d');
    // var video = document.getElementById('video');

    // // Trigger photo take
    // document.getElementById("snap").addEventListener("click", function() {
    //     context.drawImage(video, 0, 0, 640, 480);
    // });


  






// }


// (function run() {
//     navigator.getMedia = (navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia);
//     navigator.getMedia(
//         // constraints
//         {video:true, audio:false},
//         // success callback
//         function (mediaStream) {
//             var video = document.getElementsByTagName('video')[0];
//             video.src = window.URL.createObjectURL(mediaStream);
//             video.play();
//         },   
//         //handle error
//         function (error) {
//             console.log(error);
//         })   
// 	}
// )
// ();

