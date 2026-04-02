# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

VibeFinder 1.0 suggests songs from a small catalog based on a user's preferred genre, mood, energy level, and acoustic preference. It is designed for classroom exploration of how content-based recommendation systems work — not for real-world deployment. It assumes the user can clearly state their preferences upfront and that those preferences stay constant.

---

## 3. How the Model Works

The system looks at each song in the catalog and compares it to what the user told us they like. It awards points for matches: a genre match is worth the most (2 points), a mood match is worth 1 point, and energy closeness adds up to 1.5 points depending on how close the song's energy level is to what the user wants. If the user prefers acoustic music and the song is mostly acoustic, it gets a small bonus too. Every song gets a total score, and the top 5 are returned along with a plain-language explanation of why each one ranked where it did.

---

## 4. Data

The catalog contains 10 songs stored in a CSV file. Genres represented include pop, rock, lofi, and electronic. Moods include happy, chill, and intense. The dataset is small and skewed — there are no acoustic genre songs, no jazz, no classical, and no R&B. Most songs lean toward pop and electronic, which means users with those preferences get better results than users with niche tastes. The data reflects a fairly narrow slice of what music actually sounds like across cultures and styles.

---

## 5. Strengths

The system works well for users whose preferences match the most common genres in the catalog. A happy pop fan or a high-energy rock listener gets clearly differentiated, sensible results. The explanation feature is a genuine strength — every recommendation tells the user exactly why it was chosen, which makes the system transparent and easy to understand. The scoring logic is also simple enough to debug and adjust, which is useful for learning.

---

## 6. Limitations and Bias

The biggest limitation is the small catalog — with only 10 songs, the same tracks keep appearing across very different profiles. The genre weight of 2.0 is so dominant that it can overshadow a much better mood or energy match from a different genre. The system has no acoustic genre songs at all, so a user who prefers acoustic music never gets a genre match bonus. It also treats all preferences as equally important to all users, with no way to say "I care a lot about mood but barely about genre." This could feel unfair to users whose taste doesn't fit the pop/rock/electronic mold that the dataset was built around.

---

## 7. Evaluation

Three distinct user profiles were tested: a Happy Pop Fan (high energy, pop genre), a Chill Acoustic Listener (low energy, acoustic preference), and a High Energy Rock Fan (very high energy, rock genre). For Profile 1, results matched expectations well — genre and mood aligned with the top picks. For Profile 2, results were weaker because no songs matched the "acoustic" genre, so the system fell back on mood and acousticness scores alone. For Profile 3, Storm Runner ranked first as expected, but no songs matched the "intense" mood, which exposed a gap in the dataset. The most surprising finding was that Gym Hero kept appearing in multiple profiles because its high energy made it competitive even when genre and mood didn't match.

---

## 8. Future Work

- Expand the catalog to at least 50 songs with more diverse genres including jazz, classical, R&B, and acoustic
- Add a diversity rule that prevents the same artist from appearing more than once in the top 5
- Allow users to weight their own preferences, for example letting someone say mood matters more to them than genre
- Add tempo range matching so users who want slow or fast songs get better results

---

## 9. Personal Reflection

Building this system showed me how much a few simple numbers can shape what someone sees and hears. A weight of 2.0 on genre sounds small, but it means the algorithm will almost always push the same genre to the top regardless of everything else. That is exactly how real apps create filter bubbles — not through some complex conspiracy, but through small scoring decisions made early on that compound over millions of recommendations. The most interesting moment was seeing Gym Hero show up for both the pop fan and the rock fan just because of its energy score. It made me realize that real music taste is way more complicated than any small set of features can capture, and that human curation still matters even when the algorithm seems to be working fine.