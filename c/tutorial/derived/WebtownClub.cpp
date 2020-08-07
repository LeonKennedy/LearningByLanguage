#include "WebtownClub.hpp"
#include <iostream>

void TableTennisPlayer::Name() const
{
    std::cout << first_name << ' ' << last_name;
}

void RatedPlayer::Name() const
{
    std::cout << " rate: " << rate;
}

void TableTennisPlayer::show_self() const
{
    std::cout << "TableTennisPlayer::show_self";
}

void RatedPlayer::show_self() const
{
    std::cout << "RatedPlayer::show_self";
}

void TableTennisPlayer::v_show_self() const
{
    std::cout << "TableTennisPlayer::v_show_self";
}

void RatedPlayer::v_show_self() const
{
    std::cout << "RatedPlayer::v_show_self";
}

void play()
{
    TableTennisPlayer player1("leon", "kennedy", true);
    player1.Name();
    RatedPlayer player2("leon", "kennedy", 5, true);
    player2.Name();
    player2.hasTable();
    RatedPlayer player3(3, player1);
    player3.Name();
    TableTennisPlayer & player4 = player2;
    player4.Name();
}

void play_virtual()
{
    using namespace std;
    TableTennisPlayer player1("leon", "kennedy", true);
    RatedPlayer player2("leon", "kennedy", 5, true);
    TableTennisPlayer & ref1 = player2;
    TableTennisPlayer * p1 = &player2;
    ref1.show_self();
    std::cout << " virtual: ";
    ref1.v_show_self();
    cout << endl;
    p1->show_self();
    std::cout << " virtual: ";
    p1->v_show_self();
    cout << endl;

    RatedPlayer * p2 = (RatedPlayer *) &player1;
    p2->show_self();
    std::cout << " virtual: ";
    p1->v_show_self();
    cout << endl;
}