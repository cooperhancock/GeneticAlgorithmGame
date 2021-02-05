//Cooper Hancock

#include<fstream>
#include<string>
#include<vector>

using namespace std;

#ifndef CARD_HPP
#define CARD_HPP

enum Suit {S, D, H, C, null};

class Card{
private:
    int value;
    Suit suit;
public:
    //constructors
    Card(); //sets value to -1 and suit to "empty"
    Card(int v, const Suit& s);

    //getters
    int getValue() const;
    Suit getSuit() const;

    //setters
    void setValue(int v);
    void setString(Suit s);

    //true if card holds valid value
    bool hasValue() const;

    //overloaded operators
    bool operator==(const Card& other) const;
    bool operator!=(const Card& other) const;
    bool operator*=(const Card& other) const; //suit equality
    bool operator<(const Card& other) const;
    bool operator>(const Card& other) const;

    friend istream& operator>>(istream& in, Card& card);//Streams accept card format [value] [suit]
    friend ostream& operator<<(ostream& out, const Card& card);
    /* outputs [value] of [suit]
    ** outputs cards with following value changes:
    ** 1 - ace
    ** 11 - jack
    ** 12 - queen
    ** 13 - king
    */

    //returns standard deck as a vector of cards
    //DO NOT USE TO GENERATE A "DECK" OF CARDS, USE DECK CONSTRUCTOR
    //NOT FOR USE WITH DECK CLASS
    friend vector<Card> stdDeck();
};

#endif // CARD_HPP
