$('#drop').change(
   function () {
       
       var val1 = $('#drop option:selected').val();
       var date = val1 + '-01-2017';
       
       $.ajax({
           url: "/get_news/",
           type: "GET",
           data: { 'date': date },
           success: function (response) {
                          }
       })
       

       // Do something with val1 and val2 ...
   })

