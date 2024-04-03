function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_country_name";

    $.get(url, function (data, status) {
        console.log("got response for country names request");
        if (data) {
            var Name = data.Country;
            $('#uicountry').empty();
            $('#uicountry').append(new Option("Choose your country name"));
            for (var i =2;i<=Name.length;i++) {
                var opt = new Option(Name[i]);
                $('#uicountry').append(opt);
            }
        }
    });
}

function onClickedEstimatePrice() {
    console.log('Estimaate price button clicked');
    var Country = document.getElementById('uicountry');
    var H = document.getElementById('uih');
    var constuction_year = document.getElementById('uiyear');
    console.log(Country.value)
    console.log(H.value)
    console.log(constuction_year.value)

   

    var url = "http://127.0.0.1:5000/predict";
    var estFail=document.getElementById('uiFailure');
    var estAge=document.getElementById('uiAge')
    $.post(url, {
        Country: Country.value,
        H: H.value,
        constuction_year: constuction_year.value,
        
    }, function (data, status) {

        console.log(data.estimated_failure);
        estFail.innerHTML = Math.round(data.estimated_failure[0]);
        estAge.innerHTML= Math.round(data.estimated_failure[1]);
        console.log(status);
    });
}
window.onload = onPageLoad;