setInterval(
  function()
  {
     $.getJSON(
        $SCRIPT_ROOT + '/',
        {},
        function(data)
        {
          $("#price").text(data.result);
        });
  },
  500);   