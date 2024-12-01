use std::collections::HashMap;


fn part1(input: &Vec<(i32, i32)>) -> i32 {
    let mut result: i32 = 0;

    let mut v1: Vec<i32> = vec![];
    let mut v2: Vec<i32> = vec![];

    for (a, b) in input.iter() {
        v1.push(*a);
        v2.push(*b);
    }
    v1.sort();
    v2.sort();

    for (a,b) in v1.iter().zip(v2.iter()) {
        result += (a - b).abs();
    }

    return result;
}

fn part2(input: &Vec<(i32, i32)>) -> i32 {
    let mut result: i32 = 0;

    let mut counts = HashMap::new();

    for (_a,b) in input.iter() {
        counts.entry(b).and_modify(|x| (*x)+=1).or_insert(1);
    }

    for (a,_b) in input.iter() {
        result += a * (*counts.get(a).unwrap_or(&0));
    }

    return result;
}

pub fn run() {
    let input: Vec<(i32, i32)> = include_str!("./day_01.txt")
        .lines()
        .map(|x| x.trim())
        .map(|x| x.split_once(" "))
        .map(|x| x.unwrap())
        .map(|(x,y)| (x.parse().unwrap(), y.parse().unwrap()))
        .collect();

    println!("1.a: {:?}", part1(&input));
    println!("1.b: {:?}", part2(&input));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        let input: Vec<(i32, i32)> = vec![
            (3,   4),
        (4,   3),
        (2,   5),
        (1,   3),
        (3,   9), (3,   3)
        ];
        assert_eq!(part1(&input), 11);
    }

    #[test]
    fn test_p2() {
        let input: Vec<(i32, i32)> = vec![
            (3,   4),
        (4,   3),
        (2,   5),
        (1,   3),
        (3,   9), (3,   3)
        ];
        assert_eq!(part2(&input), 31);
    }
}
