/* ------------------------------------------------------------------------------
 *
 *  # Echarts - chart combinations
 *
 *  Chart combination configurations
 *
 *  Version: 1.0
 *  Latest update: August 1, 2015
 *
 * ---------------------------------------------------------------------------- */

$(function () {

    // Set paths
    // ------------------------------

    require.config({
        paths: {
            echarts: '/static/assets/js/plugins/visualization/echarts'
        }
    });


    // Configuration
    // ------------------------------

    require(
        // Add necessary charts
        [
            'echarts',
            'echarts/theme/limitless',
            'echarts/chart/line',
            'echarts/chart/bar',
            'echarts/chart/pie',


            'echarts/chart/scatter',
            'echarts/chart/k',
            'echarts/chart/radar',
            'echarts/chart/gauge'
        ],


        // Charts setup
        function (ec, limitless) {


            // Initialize charts
            // ------------------------------

            var line_bar = ec.init(document.getElementById('line_bar'), limitless);
            //var column_pie = ec.init(document.getElementById('column_pie'), limitless);
            //var scatter_pie = ec.init(document.getElementById('scatter_pie'), limitless);
            //var scatter_line = ec.init(document.getElementById('scatter_line'), limitless);

            var connect_pie = ec.init(document.getElementById('connect_pie'), limitless);
            var connect_column = ec.init(document.getElementById('connect_column'), limitless);

            //var candlestick_scatter = ec.init(document.getElementById('candlestick_scatter'), limitless);


            // Charts options
            // ------------------------------


            //
            // Line and bar combination
            //

            line_bar_options = {

                // Setup grid
                grid: {
                    x: 85,
                    x2: 85,
                    y: 75,
                    y2: 75
                },

                // Add tooltip
                tooltip: {
                    trigger: 'axis'
                },
                title: {
                    text: 'Crash Frequency Analysis',
                    subtext: 'Crash data',
                    sublink: 'https://www.opendataphilly.org/dataset/vehicular-crash-data/resource/5e142f82-b435-4053-9c1b-d47d7ac69b4e',

                },

                // Display data zoom
                dataZoom: {
                    show: true,
                    realtime: true,
                    start: 20,
                    end: 80
                },

                // Enable drag recalculate
                calculable: true,

                // Add legend
                legend: {
                    data: ['Crash Count', 'Person Count', 'Vehicle Count']
                },

                // Horizontal axis
                xAxis: [{
                    type: 'category',
                    data: ['2011/1', '2011/2', '2011/3', '2011/4', '2011/5', '2011/6', '2011/7', '2011/8', '2011/9', '2011/10', '2011/11', '2011/12', '2012/1', '2012/2', '2012/3', '2012/4', '2012/5', '2012/6', '2012/7', '2012/8', '2012/9', '2012/10', '2012/11', '2012/12', '2013/1', '2013/2', '2013/3', '2013/4', '2013/5', '2013/6', '2013/7', '2013/8', '2013/9', '2013/10', '2013/11', '2013/12', '2014/1', '2014/2', '2014/3', '2014/4', '2014/5', '2014/6', '2014/7', '2014/8', '2014/9', '2014/10', '2014/11', '2014/12']
                }],

                // Vertical axis
                yAxis: [
                    {
                        type: 'value',
                        name: 'Person & Vehicle',
                        axisLabel: {
                            formatter: '{value} times'
                        }
                    },
                    {
                        type: 'value',
                        name: 'Crash',
                        axisLabel: {
                            formatter: '{value} times'
                        }
                    }
                ],

                // Add series
                series: [
                    {
                        name: 'Vehicle Count',
                        type: 'bar',
                        data: [1282, 1384, 1606, 1814, 1902, 1741, 1673, 1709, 1634, 1816, 1654, 1767, 1660, 1562, 1868, 1894, 2012, 1864, 1704, 1655, 1785, 1903, 1598, 1696, 1499, 1454, 1840, 1870, 1955, 1954, 1726, 1663, 1814, 1727, 1809, 1578, 1493, 1145, 1719, 1742, 1705, 1777, 1717, 1702, 1773, 1961, 1797, 1783]
                    },
                    {
                        name: 'Person Count',
                        type: 'bar',
                        data: [1741, 1902, 2320, 2663, 2773, 2586, 2428, 2468, 2335, 2644, 2459, 2483, 2251, 2195, 2630, 2663, 2844, 2721, 2453, 2526, 2425, 2625, 2283, 2407, 2103, 1956, 2475, 2585, 2754, 2754, 2455, 2394, 2595, 2420, 2495, 2165, 1988, 1650, 2274, 2391, 2478, 2562, 2374, 2381, 2501, 2622, 2517, 2425]
                    },
                    {
                        name: 'Crash Count',
                        type: 'line',
                        yAxisIndex: 1,
                        data: [680, 721, 843, 956, 1009, 937, 881, 934, 869, 994, 884, 960, 875, 820, 970, 983, 1054, 990, 894, 929, 930, 993, 844, 914, 803, 761, 939, 986, 1052, 1024, 899, 897, 991, 882, 934, 829, 775, 610, 864, 912, 892, 912, 889, 912, 941, 1025, 958, 937]
                    }
                ]
            };


            //
            // Column and pie connection
            //

            // Pie options
            connect_pie_options = {

                // Add title
                title: {
                    text: 'Crash Vehicle Type',
                    subtext: 'Vehicle data',
                    sublink: 'https://www.opendataphilly.org/dataset/vehicular-crash-data/resource/9176ce48-9829-491e-b34c-8e5e5d782fcd',
                    x: 'center'
                },

                // Add tooltip
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },

                // Add legend
                legend: {
                    orient: 'vertical',
                    x: 'left',
                    data: ['Automobile', 'Motorcycle', 'Bus', 'Small Truck', 'Large Truck', 'SUV', 'Van', 'Others']
                },

                // Enable drag recalculate
                calculable: true,

                // Add series
                series: [{
                    name: 'Vehicle',
                    type: 'pie',
                    radius: '75%',
                    center: ['50%', '57.5%'],
                    data: [
                        {value: 52682, name: 'Automobile'},
                        {value: 1188, name: 'Motorcycle'},
                        {value: 1042, name: 'Bus'},
                        {value: 5984, name: 'Small Truck'},
                        {value: 1551, name: 'Large Truck'},
                        {value: 13570, name: 'SUV'},
                        {value: 4886, name: 'Van'},
                        {value: 10910, name: 'Others'}
                    ],

                }

                ]
            };

            // Column options
            connect_column_options = {

                // Setup grid
                grid: {
                    x: 50,
                    x2: 50,
                    y: 35,
                    y2: 55
                },

                // Add tooltip
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },

                // Add legend
                legend: {
                    data: ['Automobile', 'Motorcycle', 'Bus', 'Small Truck', 'Large Truck', 'SUV', 'Van', 'Others']
                },

                // Add toolbox
                toolbox: {
                    show: true,
                    orient: 'vertical',
                    x: 'right',
                    y: 35,
                    feature: {
                        mark: {
                            show: true,
                            title: {
                                mark: 'Markline switch',
                                markUndo: 'Undo markline',
                                markClear: 'Clear markline'
                            }
                        },
                        magicType: {
                            show: true,
                            title: {
                                line: 'Switch to line chart',
                                bar: 'Switch to bar chart',
                                stack: 'Switch to stack',
                                tiled: 'Switch to tiled'
                            },
                            type: ['line', 'bar', 'stack', 'tiled']
                        },
                        restore: {
                            show: true,
                            title: 'Restore'
                        },
                        saveAsImage: {
                            show: true,
                            title: 'Same as image',
                            lang: ['Save']
                        }
                    }
                },

                // Enable drag recalculate
                calculable: true,

                // Horizontal axis
                xAxis: [{
                    type: 'category',
                    data: ['2011', '2012', '2013', '2014']
                }],

                // Vertical axis
                yAxis: [{
                    type: 'value',
                    splitArea: {show: true}
                }],

                // Add series  ['Automobile', 'Motorcycle', 'Bus', 'Small Truck', 'Large Truck', 'SUV','Van','Others']
                series: [
                    {
                        name: 'Automobile',
                        type: 'bar',
                        stack: 'Total',
                        data: [13570, 13749, 13314, 12049]
                    },
                    {
                        name: 'Motorcycle',
                        type: 'bar',
                        stack: 'Total',
                        data: [304, 331, 265, 288]
                    },
                    {
                        name: 'Bus',
                        type: 'bar',
                        stack: 'Total',
                        data: [302, 267, 255, 214]
                    },
                    {
                        name: 'Small Truck',
                        type: 'bar',
                        stack: 'Total',
                        data: [1299, 1604, 1809, 1272]
                    },
                    {
                        name: 'Large Truck',
                        type: 'bar',
                        stack: 'Total',
                        data: [314, 405, 371, 461]
                    },
                    {
                        name: 'SUV',
                        type: 'bar',
                        stack: 'Total',
                        data: [2857, 3175, 3331, 4207]
                    },
                    {
                        name: 'Van',
                        type: 'bar',
                        stack: 'Total',
                        data: [1090, 1191, 1187, 1418]
                    },
                    {
                        name: 'Others',
                        type: 'bar',
                        stack: 'Total',
                        data: [2597, 2831, 2798, 2684]
                    }
                ]
            };

            // Connect charts
            connect_pie.connect(connect_column);
            connect_column.connect(connect_pie);


            // Apply options
            // ------------------------------

            line_bar.setOption(line_bar_options);
            connect_pie.setOption(connect_pie_options);
            connect_column.setOption(connect_column_options);


            // Resize charts
            // ------------------------------

            window.onresize = function () {
                setTimeout(function () {
                    line_bar.resize();
                    connect_pie.resize();
                    connect_column.resize();
                }, 200);
            }
        }
    );
});
