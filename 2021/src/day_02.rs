use std::str::FromStr;
use std::num::ParseIntError;

struct Direction {
    dir: char,
    num: u32
}

impl FromStr for Direction {
    type Err = ParseIntError;

    fn from_str(line: &str) -> Result<Self, Self::Err> {
        let split: Vec<&str> = line.split(" ").collect();
        let dir: char = split[0].chars().nth(0).unwrap();
        let num: u32 = split[1].parse().unwrap();

        Ok(Direction{dir, num})
    }
}

fn part1(input: &Vec<Direction>) -> u32 {
    let mut depth: u32 = 0;
    let mut horiz: u32 = 0;

    for x in input.iter() {
        match x.dir {
            'u' => {depth -= x.num},
            'd' => {depth += x.num},
            'f' => {horiz += x.num},
            _ => eprintln!("error matching")
        }
    }

    return depth * horiz;
}

fn part2(input: &Vec<Direction>) -> u32 {
    let mut depth: u32 = 0;
    let mut horiz: u32 = 0;
    let mut angle: u32 = 0;

    for x in input.iter() {
        match x.dir {
            'u' => {angle -= x.num},
            'd' => {angle += x.num},
            'f' => {horiz += x.num; depth += angle * x.num},
            _ => eprintln!("error matching")
        }
    }

    return depth * horiz;
}

pub fn run() {
    let input: Vec<Direction> = include_str!("./day_02.txt")
        .lines()
        .map(|x| x.trim())
        .map(|x| x.parse().unwrap())
        .collect();

    println!("2.a: {:?}", part1(&input));
    println!("2.b: {:?}", part2(&input));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        let input: Vec<Direction> = vec![Direction{dir:'f', num:5}, Direction{dir:'d', num:5}, Direction{dir:'f', num:8}, Direction{dir:'u', num:3}, Direction{dir:'d', num:8}, Direction{dir:'f', num:2}];
        assert_eq!(part1(&input), 150);
    }

    #[test]
    fn test_p2() {
        let input: Vec<Direction> = vec![Direction{dir:'f', num:5}, Direction{dir:'d', num:5}, Direction{dir:'f', num:8}, Direction{dir:'u', num:3}, Direction{dir:'d', num:8}, Direction{dir:'f', num:2}];
        assert_eq!(part2(&input), 900);
    }
}
