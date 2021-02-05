//Cooper Hancock

#include<string>
#include<vector>
#include "Card.hpp"

using namespace std;

#ifndef DECK_HPP
#define DECK_HPP

enum deckType {STD, WITH_JOKERS};

class Deck{
private:
    vector<Card> cards;
    int top;

    //updates top -- must be called whenever cards are added or removed from deck
    void update();

    /*//maintains order of pile, but removes all empty cards in between valid ones
    Deck& flatten();*/

public:
    /*Constructors*/

    //empty deck with no cards
    Deck();

    //***TO CODE
    //build deck of playing cards
    Deck(deckType type);

    /*UTILITY FUNCTIONS*/

    //check if card pile is empty
    bool isEmpty() const;

    //***TO CODE
    //reurns num of cards in deck
    int size() const;

    //***TO CODE
    //returns true if deck contains card
    bool contains(const Card& card) const;

    //returns true if read successfully
    //returns false and prints error if:
    //file cannot open
    //file has fewer than 11 cards
    bool readFromFile(const string& fileName);

    //***TO CODE
    //shuffles deck
    Deck shuffle();

    /*OPERATORS*/

    //"draws" top card in pile and sets it to the card param
    //top card in pile then becomes the card "underneath" the "drawn" card
    void operator>>(Card& card);

    //***TO CODE
    //"draws top card of deck and adds to the top of other deck
    //returns deck drawn from to allow for simulating dealing out cards to hands
    Deck& operator>>(Deck& other);

    //"discards" card to top of deck
    Deck& operator<<(Card& card);

    //***TO CODE
    //puts other deck into this deck
    Deck& operator<<(Deck& other);

    //outputs deck with each card on its own line
    friend ostream& operator<<(ostream& out, const Deck& deck);

    //***TO CODE
    //checks if cards in decks equal each other
    bool operator==(Deck right) const;

    //***TO CODE
    //returns deck with all cards in both decks
    Deck operator+(Deck right) const;

};

#endif // DECK_HPP
