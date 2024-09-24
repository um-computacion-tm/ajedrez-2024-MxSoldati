## 2024-09-20

### Fixed
- All the tests from pieces have their own board. Take that and keep it all together (insted of a `setUp`, with their new board, use `Board(for_test=True)`)

---

## 2024-09-19

### Added
- Finished piece moves.

### Fixed
- Refactoring pawn movements, and making a change of piece by a queen.

---

## 2024-09-09

### Added
- `test_knight`

### Vision
- Miss their moves, and I have to see were I make that, because there is an F in my test_coverage.
- Tomorrow, see what's going on with my `cli.py` ; see `pawn.py` and `knight.py` moves.

---

## 2024-09-08

### Added
- `king.py` ; `test_pawn`; `test_king`
- Imporved movements of `Queen` and `Pawn`.

### Vision
- Start with the horse, and finish it

---

## 2024-09-07

### Added
- `test_queen.py`; `test_pawn`
- Imporved movements of `Queen` and `Pawn`.

### Vision
- How I have to manage pawn movements? Too many paths from this piece

---

## 2024-09-06

### Added
- Implementation of diagonal movements for the `Bishop` piece.
- Implementation of the `Bishop` class with diagonal movement methods.
- Unit tests for the `Bishop` piece in `test_bishop.py`.
- Bug fixes in coordinate validation in the `Chess` class.
  - `validate_coords` method to check valid coordinates.
  - Unit tests for `validate_coords` in `test_chess.py`.
- Environment setup to run the CLI.

### Reflexion of this day
- Practicaly, I'm SO HAPPY, because it was a CAOS, and now I was able to solve all type of problem
- :grin: :grin: Understanding of what I'm doing :grin: :grin:
- Super brilliant idea to have started whit the `Fixing-dev` branch

---

## 2024-09-05

### Fixing
- I was knocked up with importing modules (and some fail tests), so my way to fixing this was creating a new branch where I have the main, taking some punches and winning this round jej

### Vision
- I'm going to focus on the tests of the pieces which made me fail some of the tests
-I create a new branch call `Fixing-dev` were I merge it whit the main, so I can start from a nice and good care code.

pd: in love with the process!

---

## 2024-09-03

### From class
- Looking after the movements of rook. We now have to take care of the other pieces

### Problem
- I can't understand `cli.py`

### Vision 
- Finishing the movements of all pieces and then see what happens with `cli.py`

---

## 2024-09-02

### Adding
- Queen movements; combining bishop and rook movements we have the queen movements

### Problem
- Having more problems, but being happy :sweat_smile:

---

## 2024-09-01

### Adding
- `test_bishop.py`

### Problem
- Difficulties in making the moves of the bishop

### Vision
- Taking care of bishop's possible movements, and try to finish queen, that's relatively the same moves as rook and bishop combined.
- Thinking about the king's possible moves.

---

## 2024-08-31

### Adding
- `test_chess.py`

### Problem
- When I make a `python3 -m game.cli`, and I try to move a pawn, something happens, that I can't move it. ; see this in class

---

## 2024-08-30

### Adding 
- Horizontal movements and their respective `test_rooks`

---

## 2024-08-29

### Adding 
- Fixing movements of pawn
- `test_pawn`

### Vision
- Getting confused with movements, of where were black pieces and white pieces :sweat_smile: ; However, I cleaned up my mess.
- Next commit, I'm trying to make a review and see if something is missing from what I'm doing.

---

## 2024-08-28

### Adding 
- `movements.py` it's going to have all pieces movements, and their possible moves.

### Vision
- Now finished the generic moves of pieces, and their tests

---

## 2024-08-27

### Changes
- I'm going to change the way I have my pieces, where instead of having all in 'pieces', for each type of piece, have its own file.

---

## 2024-08-23 

### Removed
- `.coverage` from repo and `.coveragerc`

### Added
- In `chess.py` I included a function to validate coords, although if we `python3 cli.py`, these coords don't work

### Vision 
- Trying to make it clear how am I going to work my `board.py`, and thinking about rules of the game.
- Trying to understand why my `validate_coords` don't work as planned.

---

## 2024-08-20

### Changes
- Important changes in the repository.
- Basically, deleted all branches, leaving only `main` and `dev`, where in `dev` going to keep all changes, destroy and fix the codes, when it's ready, the branch `main` would be updated with operational code from `dev`.

---

## 2024-08-19

### Change
- `test_board.py` (correctly edited) 

---

## 2024-08-14

### Added
- Classes: `Board` (8x8), `Chess` (Turns), `Pieces` (rook & pawn)

---

## 2024-08-11

### Added
- Changelog

---

## 2024-08-10

### Fixed
- CodeClimate improved 
- TestCoverage improved

---

## 2024-08-09

### Added
- CircleCI
- Test Coverage
- Requirements
- README
- CodeClimate

### New
- Initial release

---

## 2024-08-20

### Changes
- Major repository restructuring. Deleted all branches except `main` and `dev`. The `dev` branch will be used for development and testing, and `main` will be updated with stable code from `dev`.

---

## 2024-08-19

### Changes
- Correctly edited `test_board.py`.

---

## 2024-08-14

### Additions
- Added classes: `Board` (8x8), `Chess` (Turns), and `Pieces` (rook & pawn).

---

## 2024-08-11

### Additions
- Created initial changelog.

---

## 2024-08-10

### Fixes
- Improved CodeClimate and test coverage.

---

## 2024-08-09

### Additions
- Added CircleCI, test coverage, requirements, README, and CodeClimate.

### New
- Initial release.

---