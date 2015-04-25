require 'test_helper'

class LunchItemsControllerTest < ActionController::TestCase
  setup do
    @lunch_item = lunch_items(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:lunch_items)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create lunch_item" do
    assert_difference('LunchItem.count') do
      post :create, lunch_item: { lunch_id: @lunch_item.lunch_id, name: @lunch_item.name, vegetarian: @lunch_item.vegetarian }
    end

    assert_redirected_to lunch_item_path(assigns(:lunch_item))
  end

  test "should show lunch_item" do
    get :show, id: @lunch_item
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @lunch_item
    assert_response :success
  end

  test "should update lunch_item" do
    patch :update, id: @lunch_item, lunch_item: { lunch_id: @lunch_item.lunch_id, name: @lunch_item.name, vegetarian: @lunch_item.vegetarian }
    assert_redirected_to lunch_item_path(assigns(:lunch_item))
  end

  test "should destroy lunch_item" do
    assert_difference('LunchItem.count', -1) do
      delete :destroy, id: @lunch_item
    end

    assert_redirected_to lunch_items_path
  end
end
