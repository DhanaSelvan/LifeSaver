

var config = {
    cUrl: "https://api.countrystatecity.in/v1/countries",
    cKey: "SG93eHpXQnJlcXFFZU5DeDhkajVqT1NOUWY1WUF4djZpQjltTXJHTg==",
}

let state = document.getElementById("state");
let district = document.getElementById("inputDistrict");

function loadState(){
    state.innerHTML = `<option value="">--- Select State ---</option>`;

    fetch("https://api.countrystatecity.in/v1/countries/IN/states", {headers: {"X-CSCAPI-KEY": config.cKey}})
    .then(res=>res.json())
    .then((data)=>{
        console.log(data);
        for(let stateValue of data){
            state.innerHTML += `<option value=${stateValue.iso2}>${stateValue.name}</option>`
        }
    })
    .catch(err=> console.log(err));
}

window.onload = loadState;

function loadDistrict(){
    const selectStateCode = state.value;
    district.innerHTML = `<option value="">---Select District---</option>`;

    fetch(`${config.cUrl}/IN/states/${selectStateCode}/cities`, {headers: {"X-CSCAPI-KEY": config.cKey}})
    .then(res=>res.json())
    .then((value)=>{
        console.log(value);
        for(let districtValue of value){
            district.innerHTML += `<option value=${districtValue.name}>${districtValue.name}</option>`
        }
    })
    .catch(err=> console.log(err));
}