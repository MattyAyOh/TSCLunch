class CreateLunches < ActiveRecord::Migration
  def change
    create_table :lunches do |t|
      t.string :supplier
      t.datetime :sign_up_date_time
      t.string :creator

      t.timestamps null: false
    end
  end
end
