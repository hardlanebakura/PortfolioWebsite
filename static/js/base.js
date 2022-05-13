var monthSelect = document.getElementById("month_select");
var dateSelection = document.getElementById("date_selection");
var danceClock = document.getElementById("dance_clock");

var daysInMonth = {
    "January":31,
    "February":28,
    "March":31,
    "April":30,
    "May":31,
    "June":30,
    "July":31,
    "August":31,
    "September":30,
    "October":31,
    "November":30,
    "December":31
}

var daysInWeek = {

    0:"Sunday",
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",

}

var months = [
    'January', 'February', 'March', 'April', 'May',
    'June', 'July', 'August', 'September',
    'October', 'November', 'December'
    ];

var daysDisplay = {};
for (let i = 0; i < 7; i++) daysDisplay[i] = daysInWeek[i + 1];
daysDisplay[6] = "Sunday";

var scheduledDates = [];

for (const danceDate of danceDates) {

    let scheduledDate = {"day":(parseInt(danceDate.split("/")[0]) < 10) ? danceDate.split("/")[0].substr(1) : danceDate.split("/")[0], "month":(parseInt(danceDate.split("/")[1]) < 10) ? months[parseInt(danceDate.split("/")[1].substr(1)) - 1] : months[parseInt(danceDate.split("/")[1]) - 1], "hour":danceDate.split("/")[3].replace("09:", "9:").replaceAll("00:00", "00")};
    scheduledDates.push(scheduledDate);

}

if (scheduledDates.length > 0) { getFirstDance(); }

console.log(scheduledDates);

monthSelect.addEventListener("change", event => {

    var month = monthSelect.value;
    var dates = getDaysForMonth(month);
    var numRows = Math.ceil(dates.length / 7);

    var daySelector = document.getElementById("day_selector");
    if (daySelector != undefined) daySelector.remove();

    dateSelection.insertAdjacentHTML("afterend",
    `<div id = "day_selector">
        ${(function () {

            var returnString = "";
            for (let i = 0; i < numRows + 1; i++) {

              (i == 0) ? returnString += `<div class = 'week_details'>${(function () {
                let dstring = "";
                for (let k = 0; k < 7; k++) dstring += `<div class = "day_details">${(daysDisplay[k])}</div>`;
                return dstring;
              }) ()}</div>`
              : returnString += `<div class = 'week'>${(function () {
                let dstring = "";
                for (let k = 0; k < 7; k++) dstring += `<div class = "day_menu"><div class = "day">${k + 1}</div>
                </div>`;
                return dstring;
              }) ()}</div>`

            }

            return returnString;

        })()}
    </div>`
    );

    var days = document.getElementsByClassName("day");
    console.log(days.length);
    Array.from(days).forEach(day => {

        day.innerText = dates[Array.from(days).indexOf(day)];

        if (day.innerText != "") day.insertAdjacentHTML("afterend",
        `${(function () {

                    hourString = "<div class = 'day_hours_menu'>";
                    for (let i = 0; i < 9; i++) {
                        hourString += `<div class = "hours_wrapper"><div class = 'day_hours'>${i + 9}:00 - ${i + 10}:00</div><button class = "rm_date">X</button></div>`;
                    }

                    hourString += "</div>"

                    return hourString;

                }) ()}`
        )

        dayMenu = document.getElementsByClassName("day_menu");
        dayHours = dayMenu[Array.from(days).indexOf(day)].getElementsByClassName("day_hours");
        rmDates = document.getElementsByClassName("rm_date");

        Array.from(dayHours).forEach(dayHour => {

            dayHour.addEventListener("click", event => {

                scheduledDate = {"day":day.innerText, "month":month, "hour":dayHour.innerText};
                console.log(scheduledDate);
                scheduledDates.push(scheduledDate);
                postDate(dayHour, scheduledDate);
                getFirstDance();

            })

        })


    })

            for (const rmDate of rmDates) {

            rmDate.addEventListener("click", event => {

                  scheduledDate = {"day":rmDate.parentNode.parentNode.previousElementSibling.innerText, "month":month, "hour":rmDate.previousElementSibling.innerText};
                  rmDate.style.display = "none";
                  scheduledDates.forEach(d => {

                    if (equalObjects(d, scheduledDate)) { scheduledDates.splice(scheduledDates.indexOf(d), 1); console.log(scheduledDates); }

                  })
                  rmDate.previousElementSibling.style.pointerEvents = "auto";
                  rmDate.previousElementSibling.style.backgroundColor = "#F2F1F1";
                  ajaxRequest("DELETE", scheduledDate);
                  unlockOtherHoursInSameDay(rmDate.previousElementSibling);
                  getFirstDance();

            })

        }

    scheduledDates.forEach(scheduledDate => {
        console.log(scheduledDate);
        if (scheduledDate["month"] == month) {

            Array.from(dayMenu).forEach(day => {

                if (scheduledDate["day"] == day.innerText) {

                    let dayHours = day.getElementsByClassName("day_hours");
                    Array.from(dayHours).forEach(dayHour => {

                        if (scheduledDate["hour"] == dayHour.innerText) { dayHour.parentNode.style.backgroundColor = "red"; dayHour.style.pointerEvents = "none"; dayHour.nextElementSibling.style.display = "block"; lockOtherHoursInSameDay(dayHour); }

                    })

                }

            })

        }

    })

})

function getDaysForMonth(month) {

    var days = [];
    var dates = [];
    for (let i = 0; i < 7; i++) days.push(daysInWeek[new Date(`${month} ${i+1}, 2022`).getDay()]);
    spaceDates = 7 - days.indexOf("Monday");
    for (let i = 0; i < (Math.ceil((daysInMonth[month] + spaceDates) / 7) * 7); i++) {

        var day = daysInWeek[new Date(`${month} ${i+1}, 2022`).getDay()];
        days.push(day);

        (i < spaceDates) ? dates.push("")
        : (i >= (daysInMonth[month] + spaceDates)) ? dates.push("")
        : dates.push(i - spaceDates + 1);

    }
    return dates;

}

function postDate(dateElement, scheduledDate) {

    date = dateElement.innerText;
    dateElement.parentNode.style.backgroundColor = "red";
    dateElement.style.backgroundColor = "red";
    dateElement.style.pointerEvents = "none";
    dateElement.nextElementSibling.style.display = "block";
    ajaxRequest("POST", scheduledDate);
    lockOtherHoursInSameDay(dateElement);

}

function selectDate() {

  $("form").submit(function (event) {

  event.preventDefault();

  });

}

function ajaxRequest(reqMethod, reqData) {

    $.ajax({
    type: reqMethod,
    url: "/api/",
    contentType: "application/json",
    data: JSON.stringify(reqData),
    dataType: "json"
  });

}

function equalObjects(x, y) {
  return (x && y && typeof x === 'object' && typeof y === 'object') ?
    (Object.keys(x).length === Object.keys(y).length) &&
      Object.keys(x).reduce(function(isEqual, key) {
        return isEqual && equalObjects(x[key], y[key]);
      }, true) : (x === y);
}

function lockOtherHoursInSameDay(dayElement) {

    dayElements = dayElement.parentNode.parentNode.getElementsByClassName("day_hours");
    for (const dayHour of dayElements) {

        if (dayHour != dayElement) {

            dayHour.style.pointerEvents = "none";

        }

    }

}

function unlockOtherHoursInSameDay(dayElement) {

    dayElements = dayElement.parentNode.parentNode.getElementsByClassName("day_hours");
    for (const dayHour of dayElements) {

        if (dayHour != dayElement) {

            dayHour.style.pointerEvents = "auto";

        }

    }

}

function sortListOfDicts(property) {

    var sortOrder = 1;
    if(property[0] === "-") {
        sortOrder = -1;
        property = property.substr(1);
    }

    return function (a,b) {
        var result = (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
        if (property == "month") {
            var result = (months.indexOf(a[property]) < months.indexOf(b[property])) ? -1 : (months.indexOf(a[property]) > months.indexOf(b[property])) ? 1 : 0;
        }
        return result * sortOrder;
    }

}

function getFirstDance() {

    for (const scheduledDate of scheduledDates) scheduledDate["day"] = parseInt(scheduledDate["day"]);
    scheduledDates.sort(sortListOfDicts("month"));
    s = [];
    for (const scheduledDate of scheduledDates) {

        if (scheduledDate["month"] == scheduledDates[0]["month"]) s.push(scheduledDate);

    }

    s.sort(sortListOfDicts("day"));
    (s[0] == undefined) ? danceClock.innerText = "SCHEDULE YOUR DANCE! " :  danceClock.innerText = `NEXT DATE SCHEDULED: ${Object.values(s[0]).toString().replaceAll(",", " ")}`;

}


