// be carefull manipulating the code 
import javax.swing.*;
import java.awt.*;
import java.util.Random;

public class Virus {

    public static void main(String[] args){
        try {
            JOptionPane pane = new JOptionPane("Virus");
            Random ra = new Random();
            JOptionPane.showMessageDialog(null,"Press Enter to Activate the Virus");
            Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
            int shown = 1;
            for(int i = 5;i>=0;i--){
                JDialog a = pane.createDialog(null,"Warning");
                pane.setMessage("Activated in "+(i));
                a.setModal(false);
                a.setVisible(true);
                Thread.sleep(700);
            }

            while (true) {
                for(int i=0;i<=shown;i++) {
                    JDialog a = pane.createDialog(null, "This is Virus");
                    a.setLocation(ra.nextInt((int) screenSize.getWidth() - 100), ra.nextInt((int) screenSize.getHeight()) - 100);
                    a.setModal(false);
                    a.setVisible(true);
                }
                shown++;
            }
        }catch (Exception e){
            System.out.println(e);
        }

    }
}
