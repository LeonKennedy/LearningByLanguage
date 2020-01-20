function levenshteinDynamicProgramming(data, target) {
    if (data.length < 2 || target.length < 2) return 0;

    var m = [];
    for(var i=0; i < target.length + 1; i++) {
        m[i] = [i];
    }
    // init
    for(var j=0; j< data.length + 1; j++) {
        m[0][j] = j;
    }

    var i = 1;
    var j = 1;
    while ( m[target.length].length  != data.length + 1) {
        for(var x = i; x < m.length; x++) {
            var add = data[j-1] == target[x-1] ? 0 : 1;
            var val = Math.min(m[x-1][j] + 1, m[x][j-1] + 1 , m[x-1][j-1] + add);
            m[x][j] = val;
        }

        if (j < m[0].length - 1) {
            j++;
        }
        
        for(var y = j; y < m[0].length; y++) {
            var add = data[y-1] == target[i-1] ? 0 : 1;
            var val = Math.min(m[i-1][y] + 1, m[i][y-1] + 1, m[i-1][y-1] + add);
            m[i][y] = val;
        }
        
        if (i < m.length - 1) {
            i++;
        }
       
    }
    showMatrix(m)
    distance = m[target.length][data.length]
    console.log(distance);
    return get_score(distance, target.length);
}


function showMatrix(m) {
    for( var i=0;i < m.length; i++) {
        console.log(m[i])
    }
}

function get_score(distance, target_lenght) {
    return  Math.max(0, 1 - distance / target_lenght);
}




var data = "whii39sdfjsdfhhi3n2jifsda";
var target = "whiami";

score = levenshteinDynamicProgramming(data, target);
console.log("score: " + score);