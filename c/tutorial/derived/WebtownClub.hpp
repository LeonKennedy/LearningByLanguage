#ifndef WEBTOWNCLIB_H_
#define WEBTOWNCLIB_H_
#include <string>

class TableTennisPlayer
{
    private:
        std::string first_name;
        std::string last_name;
        bool has_table;
    public:
        TableTennisPlayer(const std::string & fn, const std::string & ln, bool ht=false) 
            : first_name(fn), last_name(ln), has_table(ht) {};
        void Name() const;
        bool hasTable() const {return has_table;}
        void resetTable(bool v) { has_table = v;}
        void show_self() const;
        virtual void v_show_self() const;
};


class RatedPlayer: public TableTennisPlayer
{
    private:
        float rate;
    public:
        RatedPlayer(const std::string & fn, const std::string & ln, float r, bool ht=false) :
            TableTennisPlayer(fn, ln, ht), rate(r) {};
        RatedPlayer(float r, TableTennisPlayer & p) :
            TableTennisPlayer(p), rate(r) {};
        RatedPlayer(TableTennisPlayer * p):
            TableTennisPlayer(*p), rate(0) {};
        float getRate() {return rate;}
        void resetRate(float r) {rate = r;}
        void Name() const;
        void show_self() const;
        virtual void v_show_self() const;
};

void play();
void play_virtual();
#endif