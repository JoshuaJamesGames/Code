import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import java.awt.BorderLayout;
import java.awt.Color;

public class SimpleFrame {
   //
   public static void main(String[] args){
      JFrame demoFrame = new JFrame("I'm a Title!");
      demoFrame.setSize(400, 250);

      //Make a JPanel to put inside our JFrame
      JPanel demoPanel = new JPanel();
      //Set demoPanel size so it is not maximized
      //Half size should do
      //Also change background to gray so we can see it
      demoPanel.setSize(200, 125);
      demoPanel.setBackground(Color.lightGray);

      //Make a Label for our containers
      JLabel demoLabel = new JLabel("I am Outside");

      //Add the components to the JFrame - separately
      demoPanel.add(demoLabel, BorderLayout.PAGE_START);
      demoFrame.add(demoPanel, BorderLayout.CENTER);

      //Set the window to CLOSE when we click x
      demoFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      //Make the window appear on screen
      demoFrame.setVisible(true);
   }
}
