use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

fn dynamicArray(n: i32, queries: &[Vec<i32>]) -> Vec<i32> {
    let mut seq_list: Vec<Vec<i32>> = vec![Vec::new(); n as usize];
    let mut last_answer = 0;
    let mut result = Vec::new();

    for query in queries {
        let query_type = query[0];
        let x = query[1];
        let y = query[2];

        let idx = (x ^ last_answer) as usize % n as usize;

        match query_type {
            1 => {
                seq_list[idx].push(y);
            }
            2 => {
                let seq = &seq_list[idx];
                last_answer = seq[y as usize % seq.len()];
                result.push(last_answer);
            }
            _ => {}
        }
    }

    result
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let first_multiple_input: Vec<String> = stdin_iterator.next().unwrap().unwrap()
        .split(' ')
        .map(|s| s.to_string())
        .collect();

    let n = first_multiple_input[0].trim().parse::<i32>().unwrap();

    let q = first_multiple_input[1].trim().parse::<i32>().unwrap();

    let mut queries: Vec<Vec<i32>> = Vec::with_capacity(q as usize);

    for i in 0..q as usize {
        queries.push(Vec::with_capacity(3_usize));

        queries[i] = stdin_iterator.next().unwrap().unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();
    }

    let result = dynamicArray(n, &queries);

    for i in 0..result.len() {
        write!(&mut fptr, "{}", result[i]).ok();

        if i != result.len() - 1 {
            writeln!(&mut fptr).ok();
        }
    }

    writeln!(&mut fptr).ok();
}
