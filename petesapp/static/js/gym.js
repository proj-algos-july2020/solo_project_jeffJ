$().ready(function(){
    $('form').submit(function(e){
        e.preventDefault()
        $.ajax({
          url: '/gym',
          method: 'POST',
          data: $(this).serialize(),
          success: fuction(serverResponse){
          }
        })
      })


});