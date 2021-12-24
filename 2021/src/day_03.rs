fn part1(input: &Vec<String>) -> u32 {
    let mut gamma: u32 = 0;
    let length = input[0].len();

    for i in 0..length {
        let mut count: i32 = 0;
        for num in input.iter() {
            match num.chars().nth(i).unwrap() {
                '1' => {count+=1;},
                '0' => {count-=1;},
                _ => eprintln!("error matching")
            }
        }
        gamma <<= 1;
        if count > 0 {
            gamma += 1;
        }
    }

    return gamma * (((1 << length) - 1) ^ gamma);
}

fn part2(input: &Vec<String>) -> u32 {
    let length = input[0].len();
    let mut oxygen_mask: Vec<bool> = vec![true; input.len()];
    let mut scrubber_mask: Vec<bool> = vec![true; input.len()];

    let mut oxygen: u32 = 0;
    let mut scrubber: u32 = 0;

    for i in 0..length {
        let mut common_oxy = '0';
        let mut count_oxy: i32 = 0;
        let mut common_scrub = '0';
        let mut count_scrub: i32 = 0;

        for (idx, num) in input.iter().enumerate() {

            if oxygen_mask[idx] {
                match num.chars().nth(i).unwrap() {
                    '1' => {count_oxy+=1;},
                    '0' => {count_oxy-=1;},
                    _ => eprintln!("error matching")
                }
            }
            if scrubber_mask[idx] {
                match num.chars().nth(i).unwrap() {
                    '1' => {count_scrub+=1;},
                    '0' => {count_scrub-=1;},
                    _ => eprintln!("error matching")
                }
            }
        }

        if count_oxy >= 0 {
            common_oxy = '1';
        }
        if count_scrub >= 0 {
            common_scrub = '1';
        }

        for num in 0..input.len() {
            if oxygen_mask[num] && input[num].chars().nth(i).unwrap() != common_oxy {
                oxygen_mask[num] = false;
            }
            if scrubber_mask[num] && input[num].chars().nth(i).unwrap() == common_scrub {
                scrubber_mask[num] = false;
            }
        }
        if oxygen_mask.iter().filter(|&x| *x).count() == 1 {
            let pos = oxygen_mask.iter().position(|&x| x).unwrap();
            oxygen = isize::from_str_radix(input[pos].as_str(), 2).unwrap() as u32;
        }
        if scrubber_mask.iter().filter(|&x| *x).count() == 1 {
            let pos = scrubber_mask.iter().position(|&x| x).unwrap();
            scrubber = isize::from_str_radix(input[pos].as_str(), 2).unwrap() as u32;
        }
    }

    return oxygen * scrubber;
}

pub fn run() {
    let input: Vec<String> = include_str!("./day_03.txt")
        .lines()
        .map(|x| x.trim())
        .map(|x| x.parse())
        .map(|x| x.unwrap())
        .collect();

    println!("3.a: {:?}", part1(&input));
    println!("3.b: {:?}", part2(&input));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_p1() {
        let input: Vec<String> = vec!["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
            .iter()
            .map(|x| x.parse().unwrap())
            .collect();
        assert_eq!(part1(&input), 198);
    }

    #[test]
    fn test_p2() {
        let input: Vec<String> = vec!["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
            .iter()
            .map(|x| x.parse().unwrap())
            .collect();
        assert_eq!(part2(&input), 230);
    }
}
