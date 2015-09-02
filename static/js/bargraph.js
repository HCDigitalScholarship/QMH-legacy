var sub_data = [
    {
        year: 1817,
        InHouse: 15,
        Overall: 19,
        Admitted: 19,
        Deceased: 0,
        Average: null
    },
    {
        year: 1818,
        InHouse: 22,
        Overall: 38,
        Admitted: 23,
        Deceased: 2,
        Average: null 
    },
    {
        year: 1819,
        InHouse: 28,
        Overall: 42,
        Admitted: 20,
        Deceased: 1,
        Average: null
    },
      {
        "year": 1820,
        "InHouse": 31,
        "Overall": 47,
        "Admitted": 19,
        "Deceased": 3,
        "Average": null
    },
    {
        "year": 1821,
        "InHouse": 28,
        "Overall": 57,
        "Admitted": 26,
        "Deceased": 7,
        "Average": null
    },
    {
        "year": 1822,
        "InHouse": 33,
        "Overall": 45,
        "Admitted": 17,
        "Deceased": 1,
        "Average": null
    },
    {
        "year": 1823,
        "InHouse": 32,
        "Overall": 50,
        "Admitted": 17,
        "Deceased": 5,
        "Average": null
    },
    {
        "year": 1824,
        "InHouse": 35,
        "Overall": 53,
        "Admitted": 18,
        "Deceased": 2,
        "Average": 33
    },
    {
        "year": 1825,
        "InHouse": 39,
        "Overall": 66,
        "Admitted": 31,
        "Deceased": 1,
        "Average": 38
    },
    {
        "year": 1826,
        "InHouse": 38,
        "Overall": 62,
        "Admitted": 23,
        "Deceased": 4,
        "Average": 38
    },
    {
        "year": 1827,
        "InHouse": 37,
        "Overall": 59,
        "Admitted": 21,
        "Deceased": 1,
        "Average": 38
    },
    {
        "year": 1828,
        "InHouse": 37,
        "Overall": 56,
        "Admitted": 19,
        "Deceased": 4,
        "Average": null
    },
    {
        "year": 1829,
        "InHouse": 28,
        "Overall": 55,
        "Admitted": 18,
        "Deceased": 5,
        "Average": null
    },
    {
        "year": 1830,
        "InHouse": 35,
        "Overall": 47,
        "Admitted": 19,
        "Deceased": 2,
        "Average": 31
    },
    {
        "year": 1831,
        "InHouse": 46,
        "Overall": 66,
        "Admitted": 31,
        "Deceased": 6,
        "Average": null
    },
    {
        "year": 1832,
        "InHouse": 42,
        "Overall": 78,
        "Admitted": 32,
        "Deceased": 10,
        "Average": null
    },
    {
        "year": 1833,
        "InHouse": 43,
        "Overall": 64,
        "Admitted": 22,
        "Deceased": 2,
        "Average": 41
    },
    {
        "year": 1834,
        "InHouse": 57,
        "Overall": 88,
        "Admitted": 45,
        "Deceased": 7,
        "Average": 51
    }
];


var margin = {"top":10, "bottom":50,"right":25, "left":30};
    var w = 950 - margin.left,
    h = 500 - margin.top - margin.bottom;

var year = function(d) {
            return d.year;
        };


var xScale = d3.scale.ordinal() 
    .domain(d3.range(0, sub_data.length))    
    .rangeRoundBands([0, w], 0.06);

var x = d3.time.scale()
        .domain([new Date(1816, 11, 1), new Date(1835,1,1)])
        .range([0, w]);


var yScale = d3.scale.linear()
                .domain([0, d3.max(sub_data, function(d) {return d["Overall"];})])
                .range([0, h]);

var y = d3.scale.linear()
                .domain([0, d3.max(sub_data, function(d) {return d["Overall"];})])
                .range([h, 0]);

var tooltip = d3.select('body').append('div')
        .style('position', 'absolute')
        .style('padding', '10px 10px')
        .style('background', 'white')
        .style('font-size', '22px')
        .style('opacity', 0)
        .attr("id", "tool")
        .style('border-radius', '15px');

//Create SVG element
var svg = d3.select("#chart")
            .append("svg")
            .attr("width", w + margin.left + margin.right)
            .attr("height", h + margin.top + margin.bottom)
            .attr("id", "actualGraph")
            .append("g")
                .attr("transform", "translate("+(margin.left+25)+","+margin.top+")");

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");
    

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

// svg.append("g")
//     .attr("class","x axis")
//     .call(xAxis);


svg.append("g")
        .attr("class","x axis")
        .attr("transform", "translate("+margin.left+","+h+")")
        .call(xAxis);
        // .selectAll(".tick")
        //     .classed("minor", function(d) { return d.getHours(); });
       

svg.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(4,0)")
      .call(yAxis);

svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - (margin.left+32))
        .attr("x",0 - (h / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("# of Patients")
            .style("color", "#000080")
            .style("font-weight", "bold");


    
//Create bars
var algo = svg.selectAll("rect")
   .data(sub_data, year)
   .enter()
   .append("rect")
   .transition()
    .attr('y', function(d) {
        return h - yScale(d.Overall);
    })
    .attr("x", function(d, i) {
        return xScale(i);
    })
    .attr("width", xScale.rangeBand())
    .attr("height", function(d) {
        return yScale(d.Overall);
    })

    .attr("fill", function(d) {
        return "rgb(0, 0, " + (d["Overall"] * 3) + ")";
    })
    .delay(function(d, i) {
        return i * 40;
    })
    .duration(1000);
    

    svg.selectAll("rect")
        .on('mouseover', function(d) {

        tooltip.transition()
            .style('opacity', .9)

        tooltip.html(d.Overall)
            .style('left', (d3.event.pageX - 35) + 'px')
            .style('top',  (d3.event.pageY - 50) + 'px')


       
        d3.select(this)
            .style('opacity', .5)
            
    })

    .on('mouseout', function(d) {
        d3.select(this)
            .style('opacity', 1)
            
    })





    
    
   

    function changeGraph(subject) {
        
    

        d3.select("#actualGraph").remove();
        d3.select("#tool").remove();
        

        var xScale = d3.scale.ordinal() 
                .domain(d3.range(0, sub_data.length))    
                .rangeRoundBands([0, w], 0.06);

        var x = d3.time.scale()
                .domain([new Date(1816, 11, 1), new Date(1835,1,1)])
                .range([0, w]);


        var yScale = d3.scale.linear()
                .domain([0, d3.max(sub_data, function(d) {return d[subject];})])
                .range([0, h]);

        var y = d3.scale.linear()
                .domain([0, d3.max(sub_data, function(d) {return d[subject];})])
                .range([h, 0]);
       

        

        var tooltip = d3.select('body').append('div')
        .style('position', 'absolute')
        .style('padding', '10px 10px')
        .style('background', 'white')
        .style('font-size', '22px')
        .style('opacity', 0)
        .attr("id", "tool")
        .style('border-radius', '15px');

        //Create SVG element
        var svg = d3.select("#chart")
                    .append("svg")
                    .attr("width", w + margin.left + margin.right)
                    .attr("height", h + margin.top + margin.bottom)
                    .attr("id", "actualGraph")
                    .append("g")
                        .attr("transform", "translate("+(margin.left+25)+","+margin.top+")");

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");
            

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left");

        // svg.append("g")
        //     .attr("class","x axis")
        //     .call(xAxis);


        svg.append("g")
                .attr("class","x axis")
                .style('text-align', 'center')
                .attr("transform", "translate("+margin.left+","+h+")")
                .call(xAxis);
                // .selectAll(".tick")
                //     .classed("minor", function(d) { return d.getHours(); });
               

        svg.append("g")
              .attr("class", "y axis")
              .attr("transform", "translate(4,0)")
              .call(yAxis);

        svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - (margin.left+32))
        .attr("x",0 - (h / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("# of Patients")
            .style("color", "navy")
            .style("font-weight", "bold");
       


            
        //Create bars
        var algo = svg.selectAll("rect")
           .data(sub_data, year)
           .enter()
           .append("rect")
           .transition()
            .attr('y', function(d) {
                return h - yScale(d[subject]);
            })
            .attr("x", function(d, i) {
                return xScale(i);
            })
            .attr("width", xScale.rangeBand())
            .attr("height", function(d) {
                return yScale(d[subject]);
            })

            .attr("fill", function(d) {
                return "rgb(0, 0, " + (d[subject] * 3) + ")";
            })
            .delay(function(d, i) {
                return i * 40;
            })
            .duration(1000);
            

            svg.selectAll("rect")
                .on('mouseover', function(d) {

                tooltip.transition()
                    .style('opacity', .9)

                tooltip.html(d[subject])
                    .style('left', (d3.event.pageX - 35) + 'px')
                    .style('top',  (d3.event.pageY - 50) + 'px')


               
                d3.select(this)
                    .style('opacity', .5)
                    
            })

            .on('mouseout', function(d) {
                d3.select(this)
                    .style('opacity', 1)


            })

       

       
    }







$(document).ready(function() {
    $("#selectMe").change(function() {
     
    
        var subject = $("#selectMe").find(":selected").text();
        if (subject == "Overall Patients") {
            subject = "Overall";
        }
        else if (subject == "Patients Residing in House") {
            subject = "InHouse";
        }
        else if (subject == "Patients Admitted") {
            subject = "Admitted";
        }
        else if (subject == "Patients Who Died") {
            subject = "Deceased";
        }else {
            subject = "Average";
        };
        changeGraph(subject);
        
        
    });
 });



  




 

