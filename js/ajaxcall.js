$(document).ready(function () {
    var timeDelay = 15000;
    loadfbposts();
    loadtwposts();
    function loadfbposts() {
            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8080/getfbposts',
                success: function (html) {
                    console.log("refreshing..");
                    $('#insertdata').html(html);
                    setTimeout(loadfbposts, timeDelay);
                },
                error: function() {
                location.href = '500.html'
               	
                  setTimeout(loadfbposts, timeDelay);
                },
                timeout: 20000
            });
        }
        function loadtwposts() {
            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8080/gettweets',
                success: function (html) {
                    console.log("refreshing..");
                    $('#inserttwdata').html(html);
                    setTimeout(loadtwposts, timeDelay);
                },
                error: function() {

                    location.href = '500.html'
                  setTimeout(loadfbposts, timeDelay);
                },
                timeout: 20000
            });
        }

});
