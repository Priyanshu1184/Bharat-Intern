import java.awt.*;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class ThermoMate extends JFrame implements ActionListener {
    private JTextField inputField;
    private JComboBox<String> choice1;
    private JComboBox<String> choice2;
    private JButton Convert;
    private JLabel resultLabel;

    public ThermoMate(){
    setBackground(Color.yellow);
    setTitle("ThermoMate Your Temperature Converter");
    setSize(420,400);
    setFont(new Font("Sherif", Font.PLAIN, 20));
    setBackground(Color.yellow);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setLayout(new FlowLayout());


    JLabel inputJLabel= new JLabel("Enter Your Temperature");
    inputField = new JTextField(4);
    JLabel checkbox= new JLabel("Please Select Your Temperature Scale For Conversion");
    String s1[]={"Celsius","Fahrenheit","Kelvin"};
    String s2[]={"Celsius","Fahrenheit","Kelvin"};
    choice1= new JComboBox<>(s1);
    choice2= new JComboBox<>(s2);

    Convert = new JButton("Convert");
    Convert.addActionListener(this);
    resultLabel = new JLabel();

    add(inputJLabel);
    add(inputField);
    add(checkbox);
    add(choice1);
    add(choice2);
    add(Convert);
    add(resultLabel);

}

    public static void main(String[] args) {
        ThermoMate app= new ThermoMate();
        app.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e){
            if(e.getSource() == Convert){
                try{ double temperature = Double.parseDouble(inputField.getText());
                if(choice1.getSelectedItem()=="Celsius"&& choice2.getSelectedItem()=="Celsius"){
                    resultLabel.setText("You Have Selected Same Temperature Scale For Conversion "+temperature + " °C ");
                }
                else if(choice1.getSelectedItem()=="Celsius"&& choice2.getSelectedItem()=="Fahrenheit"){
                    double fahrenheit = (temperature * 9 / 5) + 32;
                    resultLabel.setText(temperature + " °C = " + fahrenheit + " °F");
                }
                else if(choice1.getSelectedItem()=="Celsius"&& choice2.getSelectedItem()=="Kelvin"){
                    double kelvin = temperature + 273.15;
                resultLabel.setText(temperature + " °C = " + kelvin + " K");
                }
                else if(choice1.getSelectedItem()=="Fahrenheit"&& choice2.getSelectedItem()=="Celsius"){
                    double celsius = (temperature - 32) * 5 / 9;
                    resultLabel.setText(temperature + " °F = " + celsius + " °C");
                }
                else if(choice1.getSelectedItem()=="Fahrenheit"&& choice2.getSelectedItem()=="Fahrenheit"){
                    resultLabel.setText("You Have Selected Same Temperature Scale For Conversion "+ temperature+" \u00B0F ");
                }
                else if(choice1.getSelectedItem()=="Fahrenheit"&& choice2.getSelectedItem()=="Kelvin"){
                    double kelvin = (temperature + 459.67) * 5 / 9;
                    resultLabel.setText(temperature + " °F = " + kelvin + " K");
                }
                else if(choice1.getSelectedItem()=="Kelvin"&& choice2.getSelectedItem()=="Celsius"){
                    double celsius = temperature - 273.15;
                    resultLabel.setText(temperature + " \u00B0K = " + celsius + " °C");
                }
                else if(choice1.getSelectedItem()=="Kelvin"&& choice2.getSelectedItem()=="Fahrenheit"){
                    double fahrenheit = (temperature * 9 / 5) - 459.67;
                    resultLabel.setText(temperature + " \u00B0K = " + fahrenheit + " °F");
                }
                else if(choice1.getSelectedItem()=="Kelvin"&& choice2.getSelectedItem()=="Kelvin"){
                    resultLabel.setText("You Have Selected Same Temperature Scale For Conversion "+temperature + " \u00B0K");
                }
            }
            catch(NumberFormatException ex) {
                resultLabel.setText("Invalid input");
            }
        }
    }
}
