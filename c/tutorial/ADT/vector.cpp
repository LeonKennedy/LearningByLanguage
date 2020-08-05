#include <cmath>
#include <ctime>
#include "vector.hpp"

namespace VECTOR
{
    const double Rad_to_deg = 45 /atan(1);
    void Vector::set_mag()
    {
        mag = sqrt(x * x + y * y);
    }
    void Vector::set_ang()
    {
        if (x == 0.0 && y == 0.0)
            ang = 0.0;
        else
            ang = atan2(y, x);
    }

    void Vector::set_x()
    {
        x = mag * cos(ang);
    }
    void Vector::set_y()
    {
        y = mag * sin(ang);
    }

    Vector::Vector()
    {
        x = y = mag = ang = 0.0;
        mode = RECT;
    }
    Vector::Vector(double n1, double n2, Mode form)
    {
        mode = form;
        if (form == RECT) {
            x = n1;
            y = n2;
            set_mag();
            set_ang();
        }else if (form == POL) {
            mag = n1;
            ang = n2;
            set_x();
            set_y();
        }else{
            std::cout << "Inconrrent 3rd argument to Vector() --";
            std::cout << "vector set to 0\n";
            x = y = mag = ang = 0.0;
            mode = RECT;
        }
    }
    Vector::~Vector()
    {
    }

    void Vector::reset(double n1, double n2, Mode form)
    {
        mode = form;
        if (form == RECT) {
            x = n1;
            y = n2;
            set_mag();
            set_ang();
        }else if (form == POL) {
            mag = n1;
            ang = n2;
            set_x();
            set_y();
        }else{
            std::cout << "Inconrrent 3rd argument to Vector() --";
            std::cout << "vector set to 0\n";
            x = y = mag = ang = 0.0;
            mode = RECT;
        }
    }

    void Vector::polar_mode()
    {
        mode = POL;
    }
    void Vector::rect_mode()
    {
        mode = RECT;
    }

    const Vector Vector::operator + (const Vector & b) const 
    {
        return Vector(x + b.x, y+ b.y);
    }

    Vector Vector::operator - (const Vector & v) const 
    {
        return Vector(x - v.x, y-v.y);
    }

    Vector Vector::operator - () const
    {
        return Vector(-x, -y);
    }

    Vector Vector::operator * (double n) const
    {
        return Vector(n * x, n * y);
    }

    Vector operator* (double n, const Vector & a)
    {   
        return Vector(n * a.x, n * a.y);
    }

    std::ostream & operator << (std::ostream & os, const Vector & v)
    {
        if (v.mode == Vector::RECT)
            os << "(x, y) = (" << v.x << "," << v.y << ")";
        else if (v.mode == Vector::POL){
            os << "(m, a) = (" << v.mag << ", " << v.ang * Rad_to_deg << ")";

        }else
            os << "Vector object mode is invalid";
        return os;
    }

    const Vector & Max(const Vector & v1, const Vector & v2)
    {
        if (v1.magval() > v2.magval())
            return v1;
        else
            return v2;
    }

    void play()
    {
        Vector force1(50, 60);
        Vector force2(30, 40);
        const Vector net = Max(force1 ,force2);
    }
    // N  = (D/S)^2
    void randwalk() 
    {
        using namespace std;
        cout << " == play == " << endl;
        time_t t = time(0);
        srand(t);
        cout << "time is :" << t << endl;
        double direction;
        Vector step;
        Vector result(0.0, 0.0);
        unsigned long steps = 0;
        double target;
        double dstep;

        cout << "Enter targe distance (q to quit): ";
        while (cin >> target)
        {
            cout << "Enter step length: ";
            if (!(cin >> dstep))
                break;
            while (result.magval() < target)
            {
                direction = rand() % 360;
                step.reset(dstep, direction, Vector::POL);
                result = result + step;
                steps++;
            }
            cout << "After " << steps << " steps, the subject has the following location: \n";
            cout << result << endl;
            result.polar_mode();
            cout << " or\n" << result <<endl;

            cout << "Average outward distance per step = " << result.magval() / steps << endl;

            steps = 0;
            result.reset(0.0, 0.0);
            cout << "Enter targe distance (q to quit): ";
        }

        cout << "Bye!\n";
        cin.clear();
        while (cin.get() != '\n')
            continue;
    }
}

