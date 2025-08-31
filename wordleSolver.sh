# Benjamin Belandres
# Wordle Solver

GOOD_WORDS=`cat wordleWords`

# Finding the word to test
IS_RUNNING=true
echo "\n\n\n\n\n\n\n\n\n\n\n

██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
                                                   
███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗   
██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗  
███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝  
╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗  
███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║  
╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝  

"
echo "<n>ormal   <l>egacy"
read INPUT
INPUT=$(echo "$INPUT" | tr '[:upper:]' '[:lower:]')
if [ "$INPUT" = "l" ]; then
	while $IS_RUNNING
	do

		# Getting input

		echo -n "Enter color of letter: "
		read INPUT
		INPUT=$(echo "$INPUT" | tr '[:upper:]' '[:lower:]')

		case "$INPUT" in
			"green" | "g")
				echo -n "Enter the letter: "
				read LETTER
				LETTER=$(echo "$LETTER" | tr '[:lower:]' '[:upper:]')
				echo -n "Enter the letter's position (from 0): "
				read POSITION

				LEN=$((4 - $POSITION))
				GOOD_WORDS=`echo "$GOOD_WORDS" | grep -P "(\w{$POSITION})$LETTER(\w{$LEN})"` ;;
			"yellow" | "y")
				echo -n "Enter the letter: "
				read LETTER
				LETTER=$(echo "$LETTER" | tr '[:lower:]' '[:upper:]')
				echo -n "Enter the letter's position (from 0): "
				read POSITION

				LEN=$((4 - $POSITION))
				GOOD_WORDS=`echo "$GOOD_WORDS" | grep "$LETTER"`
				GOOD_WORDS=`echo "$GOOD_WORDS" | grep -P -v "(\w{$POSITION})$LETTER(\w{$LEN})"` ;;	
			"black" | "b")
				echo -n "Enter the letter: "
				read LETTER
				LETTER=$(echo "$LETTER" | tr '[:lower:]' '[:upper:]')
				GOOD_WORDS=`echo "$GOOD_WORDS" | grep -v "$LETTER"` ;;
			"d")
				echo "$GOOD_WORDS" ;;
			"q")
				IS_RUNNING=false
				break ;;
			"help" | "h")
				echo "d recommends a word to guess\nq stops the program\n" ;;
			*)
				echo "This ain't it chief: $INPUT" ;;
		esac
	done
else
	ITERATIONS=$((0))
	LETTER_POSITION=$((0))
	while $IS_RUNNING
		do
			# Printing suggested words after the input is done
			LETTER_POSITION=$(($ITERATIONS % 5))
			if [ $LETTER_POSITION -eq 0 ] && [ $ITERATIONS != 0 ]; then
				echo "$GOOD_WORDS"
			fi

			# Getting input
			echo -n "Enter color of letter in position $LETTER_POSITION: "
			read INPUT
			INPUT=$(echo "$INPUT" | tr '[:upper:]' '[:lower:]')

			case "$INPUT" in
				"green" | "g")
					echo -n "Enter the letter: "
					read LETTER
					LETTER=$(echo "$LETTER" | tr '[:lower:]' '[:upper:]')

					LEN=$((4 - $LETTER_POSITION))
					GOOD_WORDS=`echo "$GOOD_WORDS" | grep -P "(\w{$LETTER_POSITION})$LETTER(\w{$LEN})"` 
					ITERATIONS=$(($ITERATIONS + 1)) ;;
				"yellow" | "y")
					echo -n "Enter the letter: "
					read LETTER
					LETTER=$(echo "$LETTER" | tr '[:lower:]' '[:upper:]')

					LEN=$((4 - $LETTER_POSITION))
					GOOD_WORDS=`echo "$GOOD_WORDS" | grep "$LETTER"`
					GOOD_WORDS=`echo "$GOOD_WORDS" | grep -P -v "(\w{$LETTER_POSITION})$LETTER(\w{$LEN})"` 	
					ITERATIONS=$(($ITERATIONS + 1)) ;;

				"black" | "b")
					echo -n "Enter the letter: "
					read LETTER
					LETTER=$(echo "$LETTER" | tr '[:lower:]' '[:upper:]')
					GOOD_WORDS=`echo "$GOOD_WORDS" | grep -v "$LETTER"` 
					ITERATIONS=$(($ITERATIONS + 1)) ;;
				"q")
					IS_RUNNING=false
					break ;;
				"help" | "h")
					echo "q stops the program\n" ;;
				*)
					echo "This ain't it chief: $INPUT" ;;
			esac
		done

fi

