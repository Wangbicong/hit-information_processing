/**
 * Created by wangbicong on 2017/5/12.
 */

classA = [19, 18, 18, 15, 18, 11, 16, 19, 17, 17, 20, 17, 19, 20, 20, 15, 15, 16];
classB = [19, 15, 20, 20, 17, 18, 18, 15, 16, 18, 15, 19, 20, 19, 19, 16, 17, 13, 15];

function drawHistogram(a, b) {
    var myChart = echarts.init(document.getElementById('his'));

    var option = {
        title: {
            text: '直方图'
        },
        tooltip: {},
        legend: {
            data:['A班', 'B班']
        },
        xAxis: {
            data: ['11~12', '13~14', '15~16', '17~18', '19~20'],
            name: '班级'
        },
        yAxis: {
            name: '人数'
        },
        series: [{
            name: 'A班',
            type: 'bar',
            data: a
        }, {
            name: 'B班',
            type: 'bar',
            data: b
        }],
        color: ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3']
    };

    myChart.setOption(option);
}

function drawQuantile(a, b) {
    var myChart = echarts.init(document.getElementById('qua'));

    var option = {
        title: {
            text: '分位数图'
        },
        tooltip: {},
        legend: {
            data:['A班', 'B班']
        },
        xAxis: {
            type: 'value',
            name: 'f值'
        },
        yAxis: {
            type: 'value',
            name: '分数'
        },
        series: [{
            name: 'A班',
            type: 'scatter',
            data: a
        },{
            name: 'B班',
            type: 'scatter',
            data: b
        }],
        color: ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3']
    };

    myChart.setOption(option);
}

function drawQuantile2(a) {
    var myChart = echarts.init(document.getElementById('qua2'));
    console.log(a);
    var option = {
        title: {
            text: '分位数-分位数图'
        },
        tooltip: {},
        legend: {
        },
        xAxis: {
            type: 'value',
            min: 10,
            max: 20,
            name: 'A班'
        },
        yAxis: {
            type: 'value',
            min: 10,
            max: 20,
            name: 'B班'
        },
        series: [{
            type: 'scatter',
            data: a
        }],
        color: ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3']
    };

    myChart.setOption(option);
}

function calArrayHis(target) {
    var result = [0, 0, 0, 0, 0];
    for(var i=0; i<target.length; i++){
        result[parseInt((target[i]-11)/2)] += 1;
    }
    return result;
}

function calArrayQua(target) {
    target.sort();
    var result = new Array();
    for(var i=0;i<target.length;i++){
        result.push([(i+0.5)/target.length, target[i]]);
    }
    return result;
}

function calArrayQua2(targetA, targetB) {
    var result = new Array();
    targetA.sort();
    targetB.sort();
    for(var i=0;i<targetA.length;i++){
        result.push([targetA[i], targetB[i]]);
    }
    return result;
}

function main() {
    drawHistogram(calArrayHis(classA), calArrayHis(classB));
    drawQuantile(calArrayQua(classA), calArrayQua(classB));
    drawQuantile2(calArrayQua2(classA, classB));
}

main();

