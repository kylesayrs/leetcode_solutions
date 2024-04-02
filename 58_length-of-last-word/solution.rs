impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut word_len = 0; let mut prev_char_is_space = false; for (char_index, char) in s.chars().enumerate() {
            if char == ' ' {
                prev_char_is_space = true; continue;
            } if prev_char_is_space == true {
                prev_char_is_space = false; word_len = 0;
            } word_len += 1;
        } return word_len;
    }
}
