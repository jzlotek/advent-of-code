fn part1(input: &Vec<u16>) -> u16 {
    let mut num: u16 = 0;
    let mut prev = input[0];

    for i in 1..input.len() {
        let curr: u16 = input[i];
        let res: u16 = (curr > prev) as u16;
        num += res;
        prev = curr;
    }

    return num;
}

fn part2(input: &Vec<u16>) -> u16 {
    let mut num: u16 = 0;
    let mut prev = input[0];

    for i in 3..input.len() {
        let curr: u16 = input[i];
        let res: u16 = (curr > prev) as u16;
        num += res;
        prev = input[i-2];
    }

    return num;
}

pub fn run() {
    let input: Vec<u16> = include_str!("./day_01.txt")
        .lines()
        .map(|x| x.trim())
        .map(|x| x.parse().unwrap())
        .collect();

    println!("1.a: {:?}", part1(&input));
    println!("1.b: {:?}", part2(&input));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        let input: Vec<u16> = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
        assert_eq!(part1(&input), 7);
    }

    #[test]
    fn test_p2() {
        let input: Vec<u16> = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
        assert_eq!(part2(&input), 5);
    }
}
