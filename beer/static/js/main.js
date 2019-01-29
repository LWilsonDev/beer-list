//ajax code adapted from https://www.youtube.com/watch?v=wh2Nzc9wKXM&t=0s&list=PLKILtxhEt4-RT-GkrDkJDLuRPQfSK-6Yi&index=39
$(document).ready(function(event) {
    $(document).on('click', '#like', function(event) {
        event.preventDefault();
        var pk = $(this).attr('value');
        $.ajax({
            type: 'POST',
            url: "{%url 'like_beer' %}",
            data: { 'id': pk, 'csrfmiddlewaretoken': '{{csrf_token}}' },
            dataType: 'json',
            success: function(response) {
                $('#like-section').html(response['form'])
                console.log($('#like-section').html(response['form']));
            },
            error: function(rs, e) {
                console.log(rs.responseText);
            },
        });
    });
    
    //https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_eff_animate_smoothscroll
    // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });

});
